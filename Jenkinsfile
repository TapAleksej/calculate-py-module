def GIT_URL="git@github.com:TapAleksej/calculate-py-module.git"
pipeline {
  agent any

  environment {
    PRJ_NAME = "calc"
    VENV_DIR = "${env.WORKSPACE}/${env.PRJ_NAME}/venv"
  }

	  stages {
		stage('Checkout') {
		  steps {
			script {
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
				  cacheName: "venv-cache-${env.PRJ_NAME}",
				  path: "${env.WORKSPACE}/${env.PRJ_NAME}/venv"
				)
			  ]
			) {
			  sh """
				cd ${env.WORKSPACE}/${env.PRJ_NAME}
				echo "${env.WORKSPACE}/${env.PRJ_NAME}"
				if [ ! -d venv ]; then
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
	}
}
