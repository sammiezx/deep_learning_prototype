import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def screen_data(df, discrete_threshold = 7, skip=[]):
    df = df.drop(skip, axis=1).copy()
    
    fig, axes = plt.subplots(nrows=len(df.columns), ncols=1, figsize=(8, 2 * len(df.columns)))
    fig.tight_layout(pad=3.0)

    for i, column in enumerate(df.columns):
        if column in skip:
            next
        ax = axes[i]
        if df[column].nunique() <= discrete_threshold and df[column].dtype.name == 'object':
            # Discrete values (up to 7), for categorical columns
            value_counts = df[column].value_counts().nlargest(7)
            sns.barplot(x=value_counts.index, y=value_counts.values, ax=ax)
            
            total_count = df[column].count()
            shown_count = value_counts.sum()
            dropped_count = total_count - shown_count

            ax.set_title(f'Value Distribution - {column} (Total: {total_count}, Shown: {shown_count}, Dropped: {dropped_count})')
        else:
            try:
                df[column] = pd.to_numeric(df[column], errors='coerce')
                sns.kdeplot(df[column], ax=ax)
                total_count = df[column].count()
                ax.set_title(f'Value Distribution - {column} (Total: {total_count}, Shown: {total_count}, Dropped: 0)')
            except:
                sns.histplot(df[column], ax=ax)
                total_count = df[column].count()
                ax.set_title(f'Value Distribution - {column} (Total: {total_count}, Shown: {total_count}, Dropped: 0)')

        ax.set_xlabel('Values')
        ax.set_ylabel('Count/Density')

    plt.savefig('prepare_v1.png')
    plt.show()
