pipeline{
	agent any
	stages("automation"){
		stage("playurl-downurl"){
			steps{
				git credentialsId: '2cb0bb23-1f8a-498c-b6f4-00cc0fcc37ac', url: 'https://github.com/jack-wsy/school.git'
				sh label: '', script: 'robot --pythonpath . tc'
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

