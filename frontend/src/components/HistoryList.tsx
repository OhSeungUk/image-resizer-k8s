"use client";
import { useEffect, useState } from "react";

interface ImageRecord {
  id: number;
  filename: string;
  original_filename: string;
  created_at: string;
}

// 부모(Page)가 업로드 성공하면 리스트를 갱신하라고 신호(refreshKey)를 줌
export default function HistoryList({ refreshKey }: { refreshKey: number }) {
  const [history, setHistory] = useState<ImageRecord[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/images/history")
      .then((res) => res.json())
      .then((data) => setHistory(data))
      .catch(console.error);
  }, [refreshKey]); // refreshKey가 변할 때마다 재실행

  return (
    <div className="w-full max-w-md mt-10">
      <h2 className="text-xl font-bold mb-4 text-gray-700">📜 변환 기록</h2>
      <ul className="bg-white rounded-lg shadow divide-y">
        {history.map((item) => (
          <li key={item.id} className="p-4 flex justify-between items-center hover:bg-gray-50">
            <div>
              <p className="font-medium text-gray-800 truncate w-40">{item.original_filename}</p>
              <p className="text-xs text-gray-500">{new Date(item.created_at).toLocaleString()}</p>
            </div>
            <a 
              href={`http://localhost:8000/static/${item.filename}`} 
              target="_blank" 
              className="text-blue-500 text-sm hover:underline"
            >
              보기
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}