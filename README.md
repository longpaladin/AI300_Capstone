# aug24-p13

Codebase author(s): Pang Jin Jia

Website URL of deployed Flask web app: http://ec2-3-107-156-178.ap-southeast-2.compute.amazonaws.com

Details of CatBoost model: 
Using GridSearchCV, cv = 5, the best parameters are:
- learning rate: 0.01
- l2 leaf reg: 1
- depth: 4
- AUC score: 0.91009
Offline AUC: 0.9031 (train-test split)