# Grading_Environment

This is the grading environment used for grading assignments in Computer Science 228 at Iowa State University

#### <h2>Dependencies:</h2>

Gradle 4.2.x or higher   https://gradle.org/install/
<br>
python3                  https://www.python.org/downloads/

#### <h2>Setup:</h2>
    //Clone Repository
    $ git clone https://github.com/ComS228-TA/Grading_Environment.git
    
    //Go into the correct folder
    $ cd Grading_Environment/GradingScript228000/

    //Run One Time Setup Script
    $ sh one_time_setup.sh

    //Go into JSON Attributes folder
    $ cd json_attributes

    //Inside GraderAttributes.json, fill in the TODOs
    $ vi GraderAttributes.json

That should be it!

#### <h2>Scripts and how to use them:</h2>
<span style="color:red">*Make sure to be inside the GradingScript228000 directory to run these scripts correctly*</span>
<br>
setup_assignment:
<br>
Creates the folders necessary to start grading a new assignment. Arguements: <assignment name> Needs to be HWX, where X is the assignment number
<br>
#### Example:
    //To create folders for assignment 1
    $ sh setup_assignment.sh HW1
