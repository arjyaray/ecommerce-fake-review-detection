"Dataset excluded due to size limits. Download link in README." 
### Dataset Overview
- The dataset contains 1000 rows and 2 columns.
- The main text column appears to be `review`.
- The target label column is `liked`.

### Missing Values Observation
- Some reviews contain missing text values.
- Labels are complete with no missing values.
- Missing values will be handled during preprocessing.

### Class Distribution
- The dataset is equally balanced.
- Genuine reviews are similar in value to fake reviews.

### Text Observation
- Fake reviews appear more promotional and repetitive.
- Genuine reviews contain more specific details and experiences.
- Review lengths vary significantly.

### EDA Summary
- Dataset loaded successfully.
- Some missing values are present.
- The dataset is class-imbalanced.
- Text patterns differ between fake and genuine reviews.
- Preprocessing and modeling will be done in the next step.

### Dataset Overview
- Text column: Review
- Label column: Liked
- Dataset contains short restaurant reviews


### Preprocessing Observations
- Cleaned text is lowercase and noise-free
- URLs and punctuation are removed
- Stopwords are removed
- Text is now suitable for vectorization


### Summary
- Preprocessing applied successfully
- Cleaned text stored in `cleaned_review`
- Dataset is ready for feature extraction



