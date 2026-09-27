import numpy as np

def bootstrap_mean_difference_ci(data_group1, data_group2, num_bootstrap_samples=10000, ci_level=0.95):
    """
    Calculates the bootstrap confidence interval for the difference in means between two groups.

    Args:
        data_group1 (pd.Series or np.array): Sales data for the first group.
        data_group2 (pd.Series or np.array): Sales data for the second group.
        num_bootstrap_samples (int): Number of bootstrap samples to generate.
        ci_level (float): Confidence level for the interval (e.g., 0.95 for 95% CI).

    Returns:
        tuple: (lower_bound, upper_bound) of the confidence interval.
    """
    n1 = len(data_group1)
    n2 = len(data_group2)
    
    # Store the differences in means from each bootstrap sample
    bootstrap_differences = []

    for _ in range(num_bootstrap_samples):
        # Resample with replacement for each group
        bootstrap_sample1 = np.random.choice(data_group1, size=n1, replace=True)
        bootstrap_sample2 = np.random.choice(data_group2, size=n2, replace=True)
        
        # Calculate the difference in means for this bootstrap sample
        diff = np.mean(bootstrap_sample2) - np.mean(bootstrap_sample1)
        bootstrap_differences.append(diff)
    
    # Calculate the percentile-based confidence interval
    lower_percentile = (1 - ci_level) / 2 * 100
    upper_percentile = (1 + ci_level) / 2 * 100
    
    lower_bound = np.percentile(bootstrap_differences, lower_percentile)
    upper_bound = np.percentile(bootstrap_differences, upper_percentile)
    
    return lower_bound, upper_bound, bootstrap_differences # Also return the distribution for plotting if needed

