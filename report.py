import pandas as pd

df = pd.read_csv('exam_results.csv')
summary = []

for exam in df['Exam Name'].unique():
    exam_df = df[df['Exam Name'] == exam]
    num_candidates = exam_df['Candidate ID'].nunique()
    
    num_passed = (exam_df['Grade'] == 'Pass').sum()
    num_failed = (exam_df['Grade'] == 'Fail').sum()
    
    best_score = exam_df['Score'].max()
    worst_score = exam_df['Score'].min()
    
    summary.append({
        'Exam Name': exam,
        'Number of Candidates': num_candidates,
        'Number of Passed Exams': num_passed,
        'Number of Failed Exams': num_failed,
        'Best Score': best_score,
        'Worst Score': worst_score
    })

report_df = pd.DataFrame(summary)


report_df = report_df[
    ['Exam Name', 'Number of Candidates', 'Number of Passed Exams', 
     'Number of Failed Exams', 'Best Score', 'Worst Score']
]

print(report_df)
