pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DeveshKapil/Devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt || true'
                sh 'pip3 install selenium pytest pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --html=reports/report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: "Python Selenium Test Report"
                ])
            }
        }
    }

    post {
        always {
            emailext (
                to: '9012521291khajan@gmail.com',
                subject: "Python Selenium Test Execution Report",
                body: "The Selenium tests have finished. View the report: ${BUILD_URL}Python_Selenium_Test_Report/",
                attachLog: true
            )
        }
    }
}
