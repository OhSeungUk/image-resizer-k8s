"use client";
import { useState } from "react";
import ImageUploader from "@/components/ImageUploader";
// import HistoryList from "@/components/HistoryList";  <-- 이 줄 삭제 또는 주석 처리

export default function Home() {
  const [resultUrl, setResultUrl] = useState<string | null>(null);
  // const [refreshKey, setRefreshKey] = useState(0);   <-- 이 줄 삭제 (이제 필요 없음)

  const handleSuccess = (url: string) => {
    setResultUrl(url);
    // setRefreshKey(prev => prev + 1);                 <-- 이 줄 삭제
  };

  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-10 gap-8">
      <h1 className="text-4xl font-bold text-gray-800">🖼️ 심플 이미지 변환기 Final</h1>
      
      {/* 업로드 컴포넌트 */}
      <ImageUploader onUploadSuccess={handleSuccess} />

      {/* 결과 화면 */}
      {resultUrl && (
        <div className="mt-8 text-center animate-pulse">
          <p className="text-lg font-bold mb-2 text-green-600">변환 성공!</p>
          <img src={resultUrl} alt="Result" className="w-64 h-64 object-cover rounded-lg shadow-xl border-4 border-green-200" />
        </div>
      )}

      {/* HistoryList 컴포넌트 삭제함 */}
    </main>
  );
}