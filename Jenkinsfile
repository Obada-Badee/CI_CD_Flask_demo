pipeline {
    agent any

    stages {
        stage('Delete Older Images') {
            steps {
                sh 'docker rmi $(docker images -q) -f || true'
            }
        }

        stage('Build Docker Image'){
            script {
                env.version = "v${env.BUILD_NUMBER}"
                env.repo = "gasimxhacker/flask-server"
                sh "docker build -t ${env.repo}:${env.version} ."
                sh 'docker tag ${env.repo}:${env.version} ${env.repo}:latest'
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
                    sh 'docker push ${env.repo}:${env.version}'
                    sh 'docker push ${env.repo}:latest'
                }
            }
        }

    }
}
