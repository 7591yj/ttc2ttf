import os
from fontTools.ttLib import TTCollection


def batch_extract_ttc(source_dir="./ttc/", target_dir="./ttf/"):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".ttc"):
            input_path = os.path.join(source_dir, filename)
            collection = TTCollection(input_path)

            for i, font in enumerate(collection.fonts):
                name = font["name"].getDebugName(1) or f"font_{i}"
                # Sanitize filename to remove invalid characters
                clean_name = (
                    "".join(c for c in name if c.isalnum() or c in (" ", ".", "_", "-"))
                    .strip()
                    .replace(" ", "_")
                )

                output_filename = f"{clean_name}.ttf"
                font.save(os.path.join(target_dir, output_filename))


if __name__ == "__main__":
    batch_extract_ttc()
