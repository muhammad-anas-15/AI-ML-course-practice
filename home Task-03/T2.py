import numpy as np
import csv

np.random.seed(42)

# a) Generate Synthetic Dataset and save in .csv file

def generate_dataset(filename="students.csv"):

    n = 200 # dataset of 200 sudents

    StudentID = np.arange(1, n+1)
    Age = np.random.randint(18, 26, n)
    Attendance = np.random.uniform(40, 100, n)
    StudyHours = np.random.uniform(0, 40, n)
    Midterm = np.random.uniform(0, 100, n)
    Final = np.random.uniform(0, 100, n)

    # combine all columns
    dataset = np.column_stack((StudentID, Age, Attendance, StudyHours, Midterm, Final))

    # column names
    header = ["StudentID","Age","AttendancePercentage","StudyHoursPerWeek","MidtermScore","FinalScore"]

    with open(filename,"w",newline="") as f:
        writer = csv.writer(f)

    # write header 
        writer.writerow(header)

    # write dataset
        writer.writerows(dataset)

    print("Dataset generated and saved.")


# Load Dataset 

def load_dataset(filename="students.csv"):

  # this load the csv file into NumPy array  
    data = np.loadtxt(filename, delimiter=",", skiprows=1) # data separated by commas & skip header row.
    return data


# (b) Statistics 

def compute_statistics(data):
    numeric_data = data[:,1:]   # exclude StudentID column start from second col

    mean_vals = np.mean(numeric_data, axis=0) # calculate mean down the column values.
    median_vals = np.median(numeric_data, axis=0)
    std_vals = np.std(numeric_data, axis=0)
    min_vals = np.min(numeric_data, axis=0)
    max_vals = np.max(numeric_data, axis=0)

    return mean_vals, median_vals, std_vals, min_vals, max_vals


# (c) Correlation Matrix 

def correlation_matrix(data):
    numeric_data = data[:,1:]# exclude StudentID column start from second columns.

    return np.corrcoef(numeric_data, rowvar=False) # variables are stored in columns.


#  (d) Linear Predictor 

def predict_final(data, corr_matrix):
    mid_index = 4   # MidtermScore column 4 in numeric_data
    final_index = 5  # FinalScore column 5

    mid = data[:, mid_index]
    final = data[:, final_index]

    mean_mid = np.mean(mid)
    mean_final = np.mean(final)

    std_mid = np.std(mid)
    std_final = np.std(final)

    # correlation between midterm and final excluding studentID
    corr = corr_matrix[mid_index-1, final_index-1]

    predicted = mean_final + corr * (std_final/std_mid) * (mid - mean_mid)

    return predicted, final


# (e) Mean Absolute Error 

def mean_absolute_error(predicted, actual):
    return np.mean(np.abs(predicted - actual))


# (f) Report Writing 

def write_report(stats, corr_matrix, m):
    mean_vals = stats[0]
    median_vals = stats[1]
    std_vals = stats[2]
    min_vals = stats[3]
    max_vals = stats[4]

    columns = ["Age","Attendance","StudyHours","Midterm","Final"]

    with open("analysis_report.txt","w") as f:

        f.write("DATA ANALYSIS REPORT\n")
        f.write("----------------------------------------\n\n")

        i = 0
        for col in columns:
            f.write(f"{col}\n")
            f.write(f"Mean: {mean_vals[i]:.2f}\n")
            f.write(f"Median: {median_vals[i]:.2f}\n")
            f.write(f"Std Dev: {std_vals[i]:.2f}\n")
            f.write(f"Min: {min_vals[i]:.2f}\n")
            f.write(f"Max: {max_vals[i]:.2f}\n\n")
            i = i + 1

        f.write("\nCorrelation Matrix\n")
        f.write(str(np.round(corr_matrix,3)))
        f.write("\n\n")

        f.write(f"Mean Absolute Error of Prediction: {m}\n")

    print("Report generated.")


generate_dataset()
data = load_dataset()
stats = compute_statistics(data)
corr_matrix = correlation_matrix(data)
predicted, actual = predict_final(data, corr_matrix)


mean_absolute_error = mean_absolute_error(predicted, actual)

write_report(stats, corr_matrix, mean_absolute_error)

print("Pipeline execution completed.")