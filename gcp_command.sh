export PROJECT_ID=$(gcloud config get-value project)
export PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')

gcloud artifacts repositories create aomori --repository-format=docker --location=asia-southeast1 --description="FastAPI Skeleton"

gcloud builds submit --region=asia-southeast1 --tag asia-southeast1-docker.pkg.dev/jakartaresearch/aomori/aomori:latest

gcloud projects add-iam-policy-binding $PROJECT_ID --member=serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role=roles/run.admin

gcloud iam service-accounts add-iam-policy-binding \
    $PROJECT_NUMBER-compute@developer.gserviceaccount.com \
    --member=serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com \
    --role=roles/iam.serviceAccountUser

gcloud run deploy aomori --image asia-southeast1-docker.pkg.dev/jakartaresearch/aomori/aomori:latest --region asia-southeast1 --platform managed  \
     --args aomori.main:app,--host,0.0.0.0,--port,8080 --cpu 1 --memory 256Mi --timeout 300 --concurrency 100 \
     --set-env-vars IS_DEBUG=False,API_KEY=1103371a-e057-4874-b5b9-e96417c711f3,DEFAULT_MODEL_PATH=./sample_model/lin_reg_california_housing_model.joblib \
     --allow-unauthenticated