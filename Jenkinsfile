pipeline {
    agent any

    stages {

        stage('Build Docker Image'){
            steps {
                sh 'docker build -t gasimxhacker/flask-server:latest .'
                sh ''
            }
        }
        stage('Test API') {
            steps {
                sh 'docker run -i gasimxhacker/flask-server:latest python3 -m unittest discover tests'
            }
        }

        stage('Push') {
            steps {
                sh 'docker push gasimxhacker/flask-server:latest'
            }
        }

        stage('Deploy') {
            steps {
              sh ''
            }
        }

        stage('Echo') {
            steps {
                sh 'echo "Done"'
            }
        }
    }
}