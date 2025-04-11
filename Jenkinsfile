pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-username/ml-jenkins-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv $VENV
                source $VENV/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                source $VENV/bin/activate
                python train.py
                '''
            }
        }

        stage('Test Model') {
            steps {
                sh '''
                source $VENV/bin/activate
                python test.py
                '''
            }
        }

        stage('Deploy Model') {
            steps {
                sh '''
                mkdir -p deployed_models
                cp model/model.pkl deployed_models/
                echo "✅ Model deployed to 'deployed_models/' directory"
                '''
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up workspace...'
            cleanWs()
        }
    }
}
