
## Naive Bayes Model Overview

This project uses a **Multinomial Naive Bayes** classifier to predict whether a flight review is **recommended** or **not recommended**, based only on the text content of the review.

Naive Bayes is a probabilistic model widely used for text classification because it is simple, fast, and effective even on small datasets.

---

## How It Works

Given a review, the model estimates how likely it is to belong to each class (recommended / not recommended), based on learned word frequencies.

The prediction rule is:

```

C_final = argmax P(C) * P(D | C)

```

Where:

- **C** = class label
- **D** = document (review)
- **P(C)** = prior probability of class C
- **P(D | C)** = probability of observing review D if it belongs to class C

Since P(D) is constant across classes, it is ignored during comparison.

---

## The "Naive" Assumption

Naive Bayes assumes **conditional independence** between words, given the class:

```

P(D | C) ≈ Π P(wi | C)

```

To avoid underflow when multiplying probabilities, we work in log-space:

```

score(C) = log P(C) + Σ log P(wi | C)

```

The class with the highest score is chosen.

---

## Laplace Smoothing

If a word never appears in the training data for a class, its probability would be zero.  
Laplace smoothing fixes this:

```

P(w | C) = (count(w, C) + 1) / (total_words_in_C + V)

```

Where:

- `+1` ensures no zero probabilities
- `V` is the vocabulary size


## What This Script Does

1. Loads flight reviews from `Reviews.csv`
2. Tokenizes and normalizes the text
3. Computes:
   - Class priors
   - Word likelihoods per class
4. Converts probabilities to logarithms
5. Scores and predicts new reviews

Example:

```

Review: "Very smooth flight and friendly crew."
Prediction: positive

```
