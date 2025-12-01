@echo off
echo Building Docker image...
docker build -t rag-app .

echo Tagging image...
docker tag rag-app:latest us-central1-docker.pkg.dev/burner-ronsingh2/rag-basic/rag-app:latest

echo Pushing to Artifact Registry...
docker push us-central1-docker.pkg.dev/burner-ronsingh2/rag-basic/rag-app:latest

echo Deploying to Cloud Run...
gcloud run deploy rag-app-service ^
  --image us-central1-docker.pkg.dev/burner-ronsingh2/rag-basic/rag-app:latest ^
  --region us-central1 ^
  --platform managed ^
  --allow-unauthenticated ^
  --memory 4Gi ^
  --timeout=900

echo Deployment complete!
