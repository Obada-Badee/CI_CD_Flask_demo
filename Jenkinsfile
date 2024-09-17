pipeline {
    agent any

    stages {
        stage('Setup Environment Variables') {
            steps {
                sh 'echo "Done"'
            }
        }
    }
    post { 
        success {  
            emailext(
                to: 'obadabadee3@hotmail.com',
                subject: "Pipeline Status: SUCCESS",
                body: "Pipeline ${currentBuild.fullDisplayName} has SUCCESS.",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']])
        }  
        failure {  
            emailext(
                to: 'obadabadee3@hotmail.com',
                subject: "Pipeline Status: FAILURE",
                body: "Pipeline ${currentBuild.fullDisplayName} has FAILURE.",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']])
        }
    }
}
