pipeline{
	agent any
	stages("automation"){
		stage("playurl-downurl"){
			steps{
				git branch: 'dev', credentialsId: 'a43d19cc-b8a5-46f1-98f0-c4ab9bbaae5b', url: 'git@github.com:jack-wsy/playurl.git'
				sh label: '', script: 'robot --pythonpath . --include VR --noncritical VR tc'
				robot onlyCritical: false, outputPath: '.', passThreshold: 90.0, unstableThreshold: 40.0
			}
		}
	}
	post{
		failure{
			sh label: '', script: 'robot --pythonpath . -R output.xml -d output --noncritical VR --noncritical PC tc'
			robot onlyCritical: false, outputPath: './output', passThreshold: 90.0, unstableThreshold: 40.0
		}
	}
}

