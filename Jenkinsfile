pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git(
                url: 'https://github.com/yashwanthkothi/weather-app.git',
                    credentialsId: 'weather',  // Use your Jenkins credential ID
                    branch: 'main'
                )
            }
        }
        stage('Install & Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pytest test_app.py -v
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("weather-app:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-creds') {
                        docker.image("weather-app:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()  // Clean workspace
        }
    }
}
