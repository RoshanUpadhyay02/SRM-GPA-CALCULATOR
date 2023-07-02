from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate_sgpa", methods=["POST"])
def calculate_sgpa():
    num_subjects = int(request.form.get("num_subjects"))
    return render_template("subject_details.html", num_subjects=num_subjects)

@app.route("/result", methods=["POST"])
def calculate_result():
    num_subjects = int(request.form.get("num_subjects"))
    total_credits = 0
    total_grade_points = 0

    for i in range(num_subjects):
        credits = int(request.form.get(f"credits_{i}"))
        grade = request.form.get(f"grade_{i}")
        print(credits, grade)
        grade_points = calculate_grade_points(grade)
        total_credits += credits
        total_grade_points += credits * grade_points

    sgpa = total_grade_points / total_credits

    return render_template("result.html", sgpa=sgpa, num_subjects=num_subjects, total_credits=total_credits, total_grade_points=total_grade_points)

def calculate_grade_points(grade):
    grade_points_mapping = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5 , "F": 0, "Ab": 0, "I": 0}
    return grade_points_mapping.get(grade, 0)

if __name__ == "__main__":
    app.run()
