import fitz


def pdf_data_extractor(path_pdf) -> str:
    try:

        doc = fitz.open(path_pdf)
        pages = []

        for pagina in doc:
            
            texto = pagina.get_text()
            
            if texto:
                pages.append(texto)

        doc.close()

        return "\n".join(pages)

    except Exception:
        print(f"\033[93mWARNING: Verify file integrity since the information could not be processed {path_pdf}\033[0m")
        return None
