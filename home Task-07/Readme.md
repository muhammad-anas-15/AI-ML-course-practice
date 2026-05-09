What domain did you choose and why? What makes your dataset interesting?

    I chose the music domain to classify songs as "Bop" or "Skip" because it is simple and relatable. The dataset is interesting because multiple features together decide the outcome.

How did you generate the data? What logic governs the class labels? How did you inject noise?

    I generated 300 records with BPM, energy, and danceability. I used a scoring formula with weights and added noise to make the data realistic.

What was your optimal K? How did you find it? Include the K vs. Accuracy plot.

    I used K = √N and confirmed it using the K vs Accuracy plot. The best K is where test accuracy is highest and stable.

Which feature contributed most to classification? How do you know?

    Energy and danceability contributed the most because they had higher weights and clearly separate the classes.

What happened when you removed feature scaling ? Show before/after comparison.

    Energy and danceability contributed the most because they had higher weights and clearly separate the classes.

What are the limitations of KNN for your specific dataset?

    KNN is slow for large data, sensitive to scaling, and affected by noise and overlapping classes.

If you could add a 4th feature, what would it be and why?

    I would add loudness because it relates to energy and can improve classification accuracy.