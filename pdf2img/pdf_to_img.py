import os
import argparse
from pdf2image import convert_from_path

def convert_pdf_to_images(pdf_path, dpi=200, fmt="png"):
    # Extract folder and filename
    pdf_dir = os.path.dirname(pdf_path)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Create output folder next to the PDF
    output_folder = os.path.join(pdf_dir, pdf_name)
    os.makedirs(output_folder, exist_ok=True)

    # Convert PDF to images
    print(f"[+] Converting '{pdf_path}' at {dpi} DPI...")
    pages = convert_from_path(pdf_path, dpi=dpi)

    print(f"[+] Found {len(pages)} pages. Saving to {output_folder}/ …")

    image_paths = []
    for i, page in enumerate(pages, start=1):
        filename = f"page_{i:03d}.{fmt.lower()}"
        full_path = os.path.join(output_folder, filename)

        page.save(full_path, fmt.upper())
        image_paths.append(full_path)
        print(f"    - Saved: {full_path}")

    print("[✓] Done!")
    return image_paths


def main():
    parser = argparse.ArgumentParser(description="Local PDF → Image converter")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--dpi", type=int, default=200, help="Resolution (default 200)")
    parser.add_argument("--format", choices=["png", "jpeg", "jpg"], default="png", help="Image format")

    args = parser.parse_args()

    convert_pdf_to_images(
        pdf_path=args.pdf_path,
        dpi=args.dpi,
        fmt=args.format
    )


if __name__ == "__main__":
    main()
