// frontend/src/components/ImageUploader.tsx
"use client";
import { useState } from "react";

interface Props {
  onUploadSuccess: (url: string) => void; // 부모에게 URL을 전달하는 함수
}

export default function ImageUploader({ onUploadSuccess }: Props) {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    try {
      // 주소가 /images/upload 로 바뀐 것 주의!
      const res = await fetch("http://127.0.0.1:8000/images/upload", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      onUploadSuccess(data.url); // 성공 시 부모에게 알림
    } catch (e) {
      alert("업로드 실패!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 border-2 border-dashed border-gray-300 rounded-xl bg-white text-center">
      <input 
        type="file" 
        onChange={(e) => setFile(e.target.files?.[0] || null)}
        className="mb-4 text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:bg-violet-50 file:text-violet-700"
      />
      <button 
        onClick={handleUpload}
        disabled={!file || loading}
        className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 disabled:bg-gray-400"
      >
        {loading ? "변환 중..." : "업로드 & 변환"}
      </button>
    </div>
  );
}