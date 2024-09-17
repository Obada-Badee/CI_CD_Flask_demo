pipeline {
    agent any

        stages {
        stage('Setup Environment Variables') {
            steps {
               echo 'Done'
            }
        }
    }
    post { 
        success {  
            emailext(
                subject: "Pipeline Status: SUCCESS",
                body: "Pipeline ${currentBuild.fullDisplayName} has SUCCESS.",
                recipientProviders: [[$class: 'PreviousRecipientProvider']])
        }  
        failure {  
            emailext(

                subject: "Pipeline Status: FAILURE",
                body: "Pipeline ${currentBuild.fullDisplayName} has FAILURE.",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']])
        }
    }
}
