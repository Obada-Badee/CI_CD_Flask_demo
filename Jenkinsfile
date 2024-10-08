pipeline {
    agent any

     stages {
        stage('Setup Environment Variables') {
            steps {
                script {
                    env.version = "v${env.BUILD_NUMBER}"
                    env.repo = "gasimxhacker/flask-server"
                }
            }
        }

        stage('Delete Older Images') {
            steps {
                sh 'docker stop $(docker ps -q) || true'
                sh 'docker rm $(docker ps -a -q) || true'
                sh 'docker rmi $(docker images -q) -f || true'
            }
        }

        stage('Build Docker Image'){
            steps {
                sh "docker build -t ${env.repo}:${env.version} ."
                sh "docker tag ${env.repo}:${env.version} ${env.repo}:latest"
            }
        }

        stage('Test API') {
            steps {
                sh 'docker run -i gasimxhacker/flask-server:latest python3 -m unittest discover tests'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io"
                    sh "docker push ${env.repo}:${env.version}"
                    sh "docker push ${env.repo}:latest"
                }
            }
        }
    }

    post {
        always {
            sh "docker run -d -p 5000:5000 ${env.repo}:latest"
        }
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
