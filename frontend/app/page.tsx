"use client";

/**
 * Home Page — frontend/app/page.tsx
 *
 * Connected to: GET /users (backend)
 * Displays all registered users in a clean table.
 * Auto-fetches on mount. Manual refresh available.
 */

import { useState, useEffect } from "react";

// ─── Type Definition ──────────────────────────────────────────────────────────
// Mirrors the UserResponse Pydantic model from the backend.
// Keeping types in sync between frontend and backend is critical.
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

const API_BASE = "http://localhost:8000";

// ─── Component ────────────────────────────────────────────────────────────────
export default function Home() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Fetch all users from GET /users
  const fetchUsers = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await fetch(`${API_BASE}/users`);
      if (!response.ok) {
        throw new Error(`Server responded with status ${response.status}`);
      }
      const data: User[] = await response.json();
      setUsers(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unknown error occurred");
    } finally {
      setLoading(false);
    }
  };

  // Auto-fetch users when the page first loads
  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 p-8 font-sans">
      <div className="max-w-4xl mx-auto">

        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 tracking-tight">
            User Management
          </h1>
          <p className="text-gray-500 mt-1 text-sm">
            All users registered via{" "}
            <code className="bg-gray-100 px-1.5 py-0.5 rounded text-xs font-mono">
              POST /register
            </code>
          </p>
        </div>

        {/* Controls */}
        <div className="flex items-center justify-between mb-4">
          <span className="text-sm text-gray-400">
            {loading ? "Fetching..." : `${users.length} user(s) found`}
          </span>
          <div className="flex items-center gap-3">
            <a
              href={`${API_BASE}/docs`}
              target="_blank"
              rel="noopener noreferrer"
              className="text-sm text-gray-500 underline underline-offset-2 hover:text-gray-900 transition-colors"
            >
              Swagger Docs ↗
            </a>
            <button
              id="refresh-btn"
              onClick={fetchUsers}
              disabled={loading}
              className="bg-gray-900 text-white text-sm px-4 py-2 rounded-md hover:bg-gray-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              {loading ? "Loading..." : "↺ Refresh"}
            </button>
          </div>
        </div>

        {/* Error Banner */}
        {error && (
          <div className="bg-red-50 border border-red-200 text-red-700 text-sm px-4 py-3 rounded-lg mb-4">
            <span className="font-medium">Error:</span> {error}
          </div>
        )}

        {/* Empty State */}
        {!loading && !error && users.length === 0 && (
          <div className="bg-white border border-dashed border-gray-200 rounded-xl p-16 text-center">
            <p className="text-gray-400 text-sm">No users found.</p>
            <p className="text-gray-400 text-xs mt-1">
              Use{" "}
              <a
                href={`${API_BASE}/docs#/Users/register_user_register_post`}
                target="_blank"
                rel="noopener noreferrer"
                className="underline"
              >
                POST /register
              </a>{" "}
              in Swagger to add users.
            </p>
          </div>
        )}

        {/* Users Table */}
        {users.length > 0 && (
          <div className="bg-white border border-gray-200 rounded-xl overflow-hidden shadow-sm">
            <table className="w-full text-sm">
              <thead>
                <tr className="bg-gray-50 border-b border-gray-200 text-left">
                  <th className="px-6 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">
                    ID
                  </th>
                  <th className="px-6 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">
                    Name
                  </th>
                  <th className="px-6 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">
                    Email
                  </th>
                  <th className="px-6 py-3 text-xs font-semibold text-gray-500 uppercase tracking-wider">
                    Age
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-100">
                {users.map((user) => (
                  <tr
                    key={user.id}
                    className="hover:bg-gray-50 transition-colors"
                  >
                    <td className="px-6 py-4 font-mono text-gray-400 text-xs">
                      #{user.id}
                    </td>
                    <td className="px-6 py-4 font-medium text-gray-900">
                      {user.name}
                    </td>
                    <td className="px-6 py-4 text-gray-600">{user.email}</td>
                    <td className="px-6 py-4 text-gray-600">{user.age}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
