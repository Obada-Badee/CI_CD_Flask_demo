pipeline {
    agent any

    stages {

        stage('Build'){
            steps {
                sh 'sudo docker build -t gasimxhacker/flask-server:latest .'
                sh 'sudo docker run -d -p 5000:5000 gasimxhacker/flask-server:latest'
            }
        }
        stage('Test') {
            steps {
                sh 'sudo docker run -it gasimxhacker/flask-server:latest python3 -m unittest discover tests'
            }
        }

        stage('Push') {
            steps {
                sh 'sudo docker push gasimxhacker/flask-server:latest'
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