# MediNotes Pro

An AI-powered healthcare consultation assistant that helps doctors streamline their documentation workflow by generating professional summaries, action items, and patient communications from consultation notes.

## Project Overview

MediNotes Pro is a SaaS application designed for healthcare professionals. It processes consultation notes using AI to automatically generate:

- **Professional Summaries** - Structured visit summaries for doctor's records
- **Action Items** - Next steps and follow-up tasks for the healthcare provider
- **Patient Emails** - Draft communications in patient-friendly language

The application features real-time streaming of AI-generated content, secure authentication with plan-based access control, and a modern responsive interface.

## Tech Stack

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| Next.js | 16.1.3 | React framework with SSR/SSG |
| React | 19.2.3 | UI library |
| TypeScript | 5.x | Type safety |
| Tailwind CSS | 4.x | Utility-first styling |
| Clerk | 6.36.10 | Authentication & user management |
| React Markdown | 10.1.0 | Markdown rendering |
| React DatePicker | 9.1.0 | Date selection component |
| Fetch Event Source | 2.0.1 | Server-Sent Events for streaming |

### Backend
| Technology | Purpose |
|------------|---------|
| FastAPI | Python web framework |
| Uvicorn | ASGI server |
| OpenAI API | AI/LLM integration |
| PyJWT | JWT token handling |
| Pydantic | Data validation |
| fastapi-clerk-auth | Clerk authentication integration |

### Deployment
| Service | Purpose |
|---------|---------|
| Vercel | Frontend hosting & deployment |

## Project Structure

```
saas/
├── pages/                    # Next.js frontend pages
│   ├── _app.tsx             # App wrapper with Clerk auth provider
│   ├── _document.tsx        # HTML document structure
│   ├── index.tsx            # Landing/marketing page
│   └── product.tsx          # Main consultation form (protected)
├── api/                      # Python FastAPI backend
│   ├── index.py             # AI consultation endpoint
│   └── health.py            # Health check endpoint
├── styles/
│   └── globals.css          # Tailwind + custom markdown styling
├── public/                   # Static assets
├── .env.local               # Environment variables (not in repo)
├── package.json             # Node.js dependencies
├── requirements.txt         # Python dependencies
├── tsconfig.json            # TypeScript configuration
├── next.config.ts           # Next.js configuration
├── postcss.config.mjs       # PostCSS/Tailwind config
├── vercel.json              # Vercel deployment config
└── eslint.config.mjs        # ESLint configuration
```

## Features

### Landing Page
- Hero section with product value proposition
- Feature highlights with icons
- Authentication via Clerk (Sign In/Sign Up)
- Call-to-action for free trial
- Trust indicators (HIPAA Compliant, Secure, Professional)
- Responsive design with dark mode support

### Consultation Assistant (Protected)
- Patient name input
- Date of visit picker
- Consultation notes textarea
- Real-time streaming AI response
- Markdown-formatted output
- Plan-based access control (requires premium subscription)

### Authentication & Authorization
- Clerk-based user authentication
- JWT token validation on API endpoints
- Plan-based feature gating
- Protected routes with fallback to pricing table

## API Endpoints

### POST `/api`
Generate AI consultation summary with streaming response.

**Request:**
```json
{
  "patient_name": "string",
  "date_of_visit": "YYYY-MM-DD",
  "notes": "string"
}
```

**Headers:**
```
Authorization: Bearer <clerk_jwt_token>
Content-Type: application/json
```

**Response:** Server-Sent Events (text/event-stream)

### GET `/api/health`
Health check endpoint.

**Response:**
```json
{
  "status": "ok"
}
```

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.9+
- npm or yarn
- Clerk account
- OpenAI API key

### Environment Variables

Create a `.env.local` file in the root directory:

```env
# Clerk Authentication
CLERK_JWKS_URL=https://your-clerk-instance.clerk.accounts.dev/.well-known/jwks.json
CLERK_SECRET_KEY=sk_test_...
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...

# OpenAI
OPENAI_API_KEY=sk-...
```

### Installation

**Frontend:**
```bash
# Install Node.js dependencies
npm install

# Run development server
npm run dev
```

**Backend:**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn api.index:app --reload
```

### Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Create production build |
| `npm run start` | Run production server |
| `npm run lint` | Run ESLint |

## Architecture

### Data Flow
1. User submits consultation form on frontend
2. Frontend sends POST request with JWT token to `/api`
3. Backend validates JWT via Clerk JWKS
4. Request is processed through OpenAI API
5. Response streams back via Server-Sent Events
6. Frontend renders markdown in real-time

### Security
- All API endpoints require valid Clerk JWT
- User ID extracted from JWT claims for tracking
- Premium subscription required for main features
- HTTPS enforced in production

## Deployment

### Vercel (Recommended)

1. Connect your GitHub repository to Vercel
2. Configure environment variables in Vercel dashboard
3. Deploy automatically on push to main branch

### Manual Deployment

```bash
# Build the application
npm run build

# Start production server
npm run start
```

## Development Notes

### Streaming Implementation
The application uses `@microsoft/fetch-event-source` for handling Server-Sent Events, enabling real-time display of AI-generated content as it's produced.

### Markdown Rendering
AI responses are rendered using `react-markdown` with `remark-gfm` (GitHub Flavored Markdown) and `remark-breaks` for proper line break handling. Custom styling is applied via `globals.css`.

### Authentication Flow
1. User clicks Sign In on landing page
2. Clerk modal handles authentication
3. JWT token issued and stored
4. Token included in API requests
5. Backend validates via Clerk JWKS endpoint

## License

Proprietary - All rights reserved.

## Support

For questions or issues, please contact the development team.
