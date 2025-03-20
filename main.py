from PIL import Image
from fast_alpr import ALPR
import io
import uuid
import os

alpr = ALPR(
    detector_model="yolo-v9-t-384-license-plate-end2end",
    ocr_model="global-plates-mobile-vit-v2-model",
)

app = FastAPI()

@app.get("/")
async def test():
    return "ALIVE"


@app.post("/detect/")
async def extract_name_from_id(upload: UploadFile = File(...)):
    """Receives an image, applies preprocessing, performs OCR, and returns the extracted name."""
    try:
        image_data = await upload.read()
        img = Image.open(io.BytesIO(image_data))
        out_image_path =  str(uuid.uuid4())+".png"
        img.save(out_image_path)

        alpr_results = alpr.predict(out_image_path)
     #   os.remove(out_image_path)
        print(alpr_results)
        return {"Data": alpr_results}
    except Exception as e:
        return {"error": str(e)}
