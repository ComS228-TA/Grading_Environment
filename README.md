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
**Make sure to be inside the GradingScript228000 directory to run these scripts correctly**
#### <h3>setup_assignment:</h3>
Creates the folders necessary to start grading a new assignment. 
<br>
<br>
Arguments: &lt;assignment name&gt; Needs to be HWX, where X is the assignment number
#### Example:
    //To create folders for assignment 1
    $ sh setup_assignment.sh HW1
#### <h3>setup_student_files:</h3>
After having placed student zip files in HWX_Submissions and the HWXGradingTemplate in HWX folder, unzips all the students submissions and places them in HWX_Submissions_Unzipped. It also places submissions that did not have the correct files necesasry to grade the submssion in the Errors folder within HWX folder.
<br>
<br>
Arguments: &lt;assignment name&gt; Needs to be HWX, where X is the assignment number
#### Example:
    //To unzip submissions and check for errors in assignment 1
    $ sh setup_student_files.sh HW1
#### <h3>run_next_student:</h3>
Inserts the following students code into the HW_Student project. Runs gradle in the HW_Test project and places the output in the students grading file.
Runs Gradle eclipse in the HW_Student project so that the project can be open in Eclipse for further testing or debugging. If there is a compilation error or infinite loop, will notify user.
<br>
<br>
Arguments: &lt;assignment name&gt; Needs to be HWX, where X is the assignment number
#### Example:
    //To run the test script on the following students code
    $ sh run_next_student.sh
#### <h3>run_rest_of_students:</h3>
Similar to run_next_student: places the following student code in HW_Student, runs gradle in HW_Test, saves output in student grading file. However will continue on and do the same for all the other students left to grade. Will stop if a student has an error in their code such as compilation error or an infinite loop. If error occurs, simply open in Eclipse, fix the error and run again. It will not swap code in HW_Student if there was a previous error. Can still be used if you ran  run_next_student before.
<br>
<br>
Arguments: &lt;assignment name&gt; Needs to be HWX, where X is the assignment number
#### Example:
    //To run the rest of the students code with the test script for assignment 1
    sh run_rest_of_students.sh
#### <h2>If there are any questions, feel free to contact me, Jason Ramirez, at <a href="mailto:jp51371@iastate.edu">jp51371@iastate.edu</a></h2> 
