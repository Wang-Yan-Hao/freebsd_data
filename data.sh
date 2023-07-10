#!/bin/sh

# Get the current timestamp
current_time() {
  date +"%Y-%m-%d %H:%M:%S"
}

# Clone repositories
git clone git@github.com:freebsd/freebsd-doc.git
git clone git@github.com:freebsd/freebsd-src.git

# # Reset repositories to specific versions.
# # freebsd_doc_version='89fc451f1ca4ee6a83f80cde27b1dbe1f9f83d3b'
# # freebsd_src_version='e17dd921a22e846b31d99c15344ad8d0171bc7d5'
# # cd freebsd-doc && git reset --hard "$freebsd_doc_version" && cd ..
# # cd freebsd-src && git reset --hard "$freebsd_src_version" && cd ..

# Create data directories
mkdir -p data/doc/documentation
mkdir -p data/doc/website
mkdir -p data/src

echo "[INFO] Cloning and resetting repositories completed at $(current_time)"

# Get the file
cd freebsd-doc || exit
make DOC_LANG=en
cd documentation/public/ || exit

# Copy HTML files to data/doc/documentation
find . -type f -regex ".*\.html" -print0 | cpio -pd0 "../../../data/doc/documentation"

cd ../../website/public || exit

# Copy HTML files to data/doc/website
find . -type f -regex ".*\.html" -print0 | cpio -pd0 "../../../data/doc/website"

cd ../../../freebsd-src || exit

# Copy .[0-9] and .md files to data/src/
find . -type f -regex ".*\.[0-9]$" -print0 | cpio -pd0 "../data/src/"
find . -type f -regex ".*\.md$" -print0 | cpio -pd0 "../data/src/"

echo "[INFO] Copying files completed at $(current_time)"

cd ../data/src/ || exit

# Convert .[0-9] files to HTML
find . -type f -regex ".*\.[0-9]$" -exec sh -c 'mandoc -T html "$0" > "$0.html"' {} \;

# Convert .md files to plain text
find . -type f -regex ".*\.md" -exec pandoc -f markdown -t plain "{}" -o "{}.txt" \;

cd .. || exit

# Convert HTML files to plain text
find . -type f -regex ".*\.html" -exec pandoc -f html -t plain "{}" -o "{}.txt" \;

echo "[INFO] Convert files to plain text completed at $(current_time)"

cd ..

# Remove irrevelant content in the text files
find "data/doc" -type f -name "*.txt" -exec sh -c 'awk "/^\[FreeBSD logo\]$/, /^♥ Donate$/ {next} 1" "$1" > "$1.tmp" && mv "$1.tmp" "$1"' _ {} \;
find "data/doc" -type f -name "*.txt" -exec sh -c 'awk "/^trademarks$/,/^symbol\.$/ {next} 1" "$1" > "$1.tmp" && mv "$1.tmp" "$1"' _ {} \;
find "data/doc" -type f -name "*.txt" -exec sh -c 'awk "/^Resources$/,/^- Edit this page$/ {next} 1" "$1" > "$1.tmp" && mv "$1.tmp" "$1"' _ {} \;
find "data/doc" -type f -name "*.txt" -exec sh -c 'sed "/^--*$/d" "$1" > "$1.tmp" && mv "$1.tmp" "$1"' _ {} \;

echo "[INFO] Content removal completed at $(current_time)"

# Define source and destination directories
SOURCE_DIR="data/"
DESTINATION_DIR="data/data_all/"

# Check if source directory exists
if [ -d "$SOURCE_DIR" ]; then
    # Create destination directory if it doesn't exist
    mkdir -p "$DESTINATION_DIR"

    # Find all .txt files and copy them to the destination directory
    find "$SOURCE_DIR" -type f -name "*.txt" -print0 | cpio -pd0 "$DESTINATION_DIR"
else
    echo "Source directory ${SOURCE_DIR} does not exist"
fi

echo "[INFO] Script finished at $(current_time)"
