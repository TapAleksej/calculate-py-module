def GIT_URL="git@github.com:AnastasiyaGapochkina01/calculate-py-module.git"

pipeline {
  agent any

  environment {
    PRJ_NAME = "calc"
    VENV_DIR = "${env.WORKSPACE}/${env.PRJ_NAME}/venv"
  }

  stages {
    stage('Checkout') {
      if (fileExists("${env.PRJ_NAME}/.git")) {
        dir(env.PRJ_NAME) {
          sh "git pull"
        } 
      } else {
          sh "git clone ${env.GIT_URL} ${env.PRJ_NAME}"
        }
      }
    }
  }
  stage('Setup Environment') {
    steps {
      script {
        cache(
          maxCacheSize: 1,
          caches: [
            arbitraryFileCache(
              chacheName: "venv-cache-${env.PRJ_NAME}",
              path: "${env.WORKSPACE}/${env.PRJ_NAME}/venv"
            )
          ]
        ) {
          sh """
            cd ${env.PRJ_NAME}
            if [ -d venv ]; then
              python3 -m venv venv
            fi
            . venv/bin/activate
            pip install -e .
            pip install -r requirements.txt
          """
        }
      }
    }
  }
  stage('Parallel Checks)' {
    parallel {
      stage('Security Scan') {
        steps {
          script {
            sh """
              cd ${env.PRJ_NAME}
              . venv/bin/activate
              bandir -r app/ -f json -o bandit_results.json || true
            """
            archiveArtifacts artifacts: "${env.PRJ_NAME}/bandit_results.json", allowEmptyArchive: true
          }
        }
      }
      stage('Run Unit Tests') {
        steps {
          script {
            sh """
              cd ${env.PRJ_NAME}
              . venv/bin/activate
              PYTHONPATH=src pytest -v tests/ --junitxml=tests-result.xml
            """
            archiveArtifacts artifacts: "${env.PRJ_NAME}/tests-result.xml", allowEmptyArchive: true
          }
        }
      }
    }
  }
  stage('Create Module'){
    steps {
      script {
        sh """
          cd ${env.PRJ_NAME}
          . venv/bin/activate
          python setup.py bdist_wheel
        """
      }
    }
  }
  stage('Create And Archive Module') {
    steps {
      script {
        sh """
          tar -czvf ${workspace}/${env.PRJ_NAME}_${BUILD_NUMBER}.tar.gz ${env.PRJ_NAME}/dist/
        """
        archiveArtifacts artifacts: "${env.PRJ_NAME}_${BUILD_NUMBER}.tar.gz", allowEmptyArchive: false
      }
    }
  }
        
}
