pipeline {
    agent any

    environment {
        IMAGE_NAME = "divy624/dockercicd"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        WORKER_IP  = "15.206.171.220"
    }

    stages {
        stage('Code Clone') {
            steps {
                git branch: 'main',
                    credentialsId: 'githubdivyp624',
                    url: 'https://github.com/divyp624-source/restaurantApi.git'
            }
        }

        stage('Build Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhubcred',
                        usernameVariable: 'USERNAME',
                        passwordVariable: 'PASSWORD'
                    )
                ]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }

        stage('Deploy') {
            steps {
                    sh """
                        docker pull ${IMAGE_NAME}:${IMAGE_TAG} &&
                        docker stop api || true &&
                        docker rm api   || true &&
                        docker run -d --name api -p 8000:8000 ${IMAGE_NAME}:${IMAGE_TAG}
                    """
            }
        }

    }

    post {
        success {
            echo 'Application deployed successfully.'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
