from typing import List

class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)

        student_scores = {id: 0 for id in student_id}

        for i, student_report in enumerate(report):
            unique_id = student_id[i]
            for char in student_report.split(" "):
                if char in positive_set:
                    student_scores[unique_id] += 3

                elif char in negative_set:
                    student_scores[unique_id] -= 1

        res = sorted(student_scores.items(), key=lambda x: (-x[1], x[0]))

        return [student[0] for student in res][:k:]