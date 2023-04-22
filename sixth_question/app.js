const fs = require('fs');
const zlib = require('zlib');
const archiver = require('archiver');

// Define the name of the output file
const output = fs.createWriteStream('my-archive.zip');

// Create a new archiver object
const archive = archiver('zip', {
  zlib: { level: 9 } // Set the compression level (0-9)
});

// Listen for 'close' event to know when the archive is finished
output.on('close', () => {
  console.log(`${archive.pointer()} total bytes`);
  console.log('Archiver has been finalized and the output file descriptor has closed.');
});

// Listen for 'error' event in case something goes wrong
archive.on('error', (err) => {
  throw err;
});

// Pipe the output to the file
archive.pipe(output);

// Add files or directories to the archive
archive.file('file1.txt', { name: 'file1.txt' });
archive.directory('myfolder', 'myfolder');

// Finalize the archive (write the footer information)
archive.finalize();