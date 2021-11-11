class CV2PIL:    
    def cv_to_pil(cv_image):
        pil_image = cv_image.copy()
        if pil_image.ndim == 2:
            pass
        elif pil_image.shape[2] == 3:
            pil_image = cv2.cvtColor(pil_image, cv2.COLOR_BGR2RGB)
        elif pil_image.shape[2] == 4:
            pil_image = cv2.cvtColor(pil_image, cv2.COLOR_BGRA2RGBA)
        pil_image = Image.fromarray(pil_image)

        return pil_image