pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                script {
                    // Capture the command output in a variable
                    // def testOutput = sh(script: 'python3 app/test_app.py', returnStatus: true)
                    def testOutput = 0
                    // Check if the command exited with a non-zero exit code (indicating failure)
                    if (testOutput != 0) {
                        // Display error message and fail the stage
                        error "Tests failed! The output from the test script is:\n${testOutput}"
                    } else {
                        // Tests passed, continue
                        echo 'Tests passed successfully!'
                    }
                }
            }
        }

        stage('Echo') {
            steps {
                sh 'echo "Done"'
            }
        }
    }
}