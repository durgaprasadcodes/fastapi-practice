import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  logLevel: 'info',
  server: {
    watch: {
      // Enable polling to improve file change detection on networked or synced drives
      usePolling: true,
      interval: 100,
    },
    hmr: {
      protocol: 'ws',
      host: 'localhost',
      clientPort: 5174,
    },
  },
})
