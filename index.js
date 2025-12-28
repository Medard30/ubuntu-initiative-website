const { spawn } = require('child_process');

console.log('Starting Ubuntu Initiative Website...');

const python = spawn('python', ['main.py'], {
  stdio: 'inherit',
  cwd: process.cwd()
});

python.on('error', (err) => {
  console.error('Failed to start Python server:', err);
  process.exit(1);
});

python.on('close', (code) => {
  console.log(`Python server exited with code ${code}`);
  process.exit(code);
});
