import { useEffect, useState } from "react";
import api from '../service/api.js'
import { ToastContainer, toast } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'
import './Upload.css'

export default function Upload() {
    const [file, setFile] = useState(null);
    const [src, Setsrc] = useState('');
    const [res, SetRes] = useState('');
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        if (!file) return;
        const objectUrl = URL.createObjectURL(file);
        Setsrc(objectUrl);
        return () => URL.revokeObjectURL(objectUrl);
    }, [file]);

    const handleUpload = async (e) => {
        e.preventDefault();
        if (!file) return;

        setLoading(true);
        const formData = new FormData();
        formData.append("file", file);

        try {
            const response = await api.post("/upload", formData);
            SetRes(response.data.text);
            toast.success("File uploaded successfully!");
        } catch (error) {
            const detail = error.response?.data?.detail;
            toast.error(
                Array.isArray(detail)
                    ? detail[0]?.msg
                    : detail || error.message || "Upload failed"
            );
        } finally {
            setLoading(false);
        }
    };

    return (
        <form className="upload-form" onSubmit={handleUpload}>
            <ToastContainer
                pauseOnHover={false}
                autoClose={2000}
                position="bottom-right"
                theme="colored"
                limit={3}
            />

            {/* ── Two-column flex layout ── */}
            <div className="upload-layout">

                {/* LEFT — file picker card only */}
                <div className="upload-left">
                    <div className="upload-card">
                        {/* Header */}
                        <div className="upload-header">
                            <span className="upload-badge">File Uploader</span>
                            <h1 className="upload-title">Upload Your File</h1>
                            <p className="upload-subtitle">
                                Drag &amp; drop or click to select — PDF, images, documents supported
                            </p>
                        </div>

                        <hr className="upload-divider" />

                        {/* Drop zone */}
                        <div className={`upload-dropzone${file ? ' has-file' : ''}`}>
                            <input
                                id="file-input"
                                className="upload-input"
                                type="file"
                                onChange={(e) => setFile(e.target.files[0])}
                            />
                            <div className="upload-icon-wrap">
                                {file ? '📄' : '☁️'}
                            </div>
                            <span className="upload-dropzone-label">
                                {file ? 'File selected' : 'Drop file here or click to browse'}
                            </span>
                            <span className="upload-dropzone-sub">
                                {file ? '' : 'Maximum file size: 50 MB'}
                            </span>
                            {file && (
                                <span className="upload-filename">{file.name}</span>
                            )}
                        </div>
                    </div>
                </div>

                {/* RIGHT — 1. Preview  2. Upload button  3. Response text */}
                <div className="upload-right">

                    {/* 1 — PDF / file preview */}
                    {src ? (
                        <div className="upload-preview-wrap">
                            <p className="upload-preview-label">Preview</p>
                            <iframe
                                className="upload-preview-frame"
                                src={src}
                                title="Document Preview"
                            />
                        </div>
                    ) : (
                        /* Placeholder shown before any file is selected */
                        <div className="upload-right-empty">
                            <span className="upload-right-empty-icon">🖼️</span>
                            <p>Your file preview will appear here</p>
                        </div>
                    )}

                    {/* 2 — Upload button */}
                    <button
                        type="submit"
                        className={`upload-btn${loading ? ' loading' : ''}`}
                        disabled={!file || loading}
                    >
                        {loading ? 'Uploading…' : 'Upload File'}
                    </button>

                    {/* 3 — Server return text */}
                    {res && (
                        <div className="upload-response-card">
                            <p className="upload-preview-label">FastAPI Response</p>
                            <div className="upload-response">{res}</div>
                        </div>
                    )}

                </div>

            </div>

        </form>
    );
}
