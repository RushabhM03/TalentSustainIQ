document.getElementById("predictForm").addEventListener("submit", function(event) {
    // Stop form from submitting normally
    event.preventDefault();

    // Get some values from elements on the page
    var form = event.target;
    var satisfaction_level = form.querySelector("input[id='satisfaction_level']").value;
    var last_evaluation = form.querySelector("input[id='last_evaluation']").value;
    var number_project = form.querySelector("input[id='number_project']").value;
    var average_montly_hours = form.querySelector("input[id='average_montly_hours']").value;
    var time_spend_company = form.querySelector("input[id='time_spend_company']").value;
    var work_accident = form.querySelector("input[id='work_accident']").value;
    var promotion_last_5years = form.querySelector("input[id='promotion_last_5years']").value;
    var salary = form.querySelector("input[id='salary']").value;

    var data = {
        "satisfaction_level": satisfaction_level,
        "last_evaluation": last_evaluation,
        "number_project": number_project,
        "average_montly_hours": average_montly_hours,
        "time_spend_company": time_spend_company,
        "work_accident": work_accident,
        "promotion_last_5years": promotion_last_5years,
        "salary": salary
    };

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:5000/prediction");
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var response = xhr.responseText;
                console.log(response);
                document.getElementById("result").innerHTML = '<div class="alert alert-success" role="alert">' + response + '</div>';
            } else {
                console.error("Error:", xhr.status, xhr.statusText);
            }
        }
    };
    var formData = new URLSearchParams(data).toString();
    xhr.send(formData);
});
