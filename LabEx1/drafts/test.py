for column_name in columns_to_check:
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    sns.histplot(data[column_name], kde=True)
    plt.title(f'{column_name} Before Cleaning')

    # Visualize the data after cleaning
    plt.subplot(1, 2, 2)
    sns.histplot(data_cleaned[column_name], kde=True)
    plt.title(f'{column_name} After Cleaning')

    plt.tight_layout()
    plt.show()


