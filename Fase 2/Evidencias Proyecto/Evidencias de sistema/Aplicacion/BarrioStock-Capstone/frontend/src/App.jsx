import { useEffect, useState } from 'react';
import api from './services/api';
import { CheckCircle2, AlertCircle, ShoppingCart } from 'lucide-react';

export default function App() {
  const [status, setStatus] = useState('conectando...');
  const [online, setOnline] = useState(false);

  useEffect(() => {
    api.get('/health')
      .then((res) => {
        setStatus(res.data.system + ' - ' + res.data.status);
        setOnline(true);
      })
      .catch(() => {
        setStatus('Error de conexión con el Backend');
        setOnline(false);
      });
  }, []);

  return (
    <div className="min-h-screen bg-slate-100 flex flex-col items-center justify-center p-4">
      <div className="bg-white shadow-xl rounded-2xl p-8 max-w-md w-full text-center">
        <div className="flex justify-center mb-4 text-brand-500">
          <ShoppingCart size={48} />
        </div>
        <h1 className="text-2xl font-bold text-slate-800 mb-2">BarrioStock POS</h1>
        <p className="text-slate-500 text-sm mb-6">Sistema Inteligente de Ventas y FEFO</p>

        <div className={`flex items-center justify-center gap-2 p-3 rounded-lg text-sm font-medium ${
          online ? 'bg-green-50 text-green-700' : 'bg-red-50 text-red-700'
        }`}>
          {online ? <CheckCircle2 size={18} /> : <AlertCircle size={18} />}
          <span>{status}</span>
        </div>
      </div>
    </div>
  );
}