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

        stage('Run the image on the server') {
            steps {
                sh "docker stop $(docker ps -q --filter ancestor=${env.repo}:latest)"
                sh "docker rm $(docker ps -q --filter ancestor=${env.repo}:latest)"
                sh "docker run -d -p 5000:5000 ${env.repo}:latest"
            }
        }
    }

    post {  
        always {
            script {
                sh 'git show --format="%ae" HEAD > last_committer.txt'
                def lastCommitEmail = readFile 'last_committer.txt'
            }
         }  
        success {  
            emailext(to: lastCommitEmail,
                subject: "Pipeline Status: SUCCESS",
                body: "Pipeline ${currentBuild.fullDisplayName} has SUCCESS.")
        }  
        failure {  
            emailext(to: lastCommitEmail,
                subject: "Pipeline Status: FAILURE",
                body: "Pipeline ${currentBuild.fullDisplayName} has FAILURE.")
        }
    }
}
