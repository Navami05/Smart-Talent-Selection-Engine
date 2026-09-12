import './App.css'

function App() {
  return (
    <div className="app">
      <header>
        <h1>Smart Talent Selection Engine</h1>
        <p>AI-powered resume screening and candidate matching</p>
      </header>

      <main>
        <section>
          <h2>Job Description</h2>
          <p>Upload a Job Description to begin candidate matching.</p>

          <input type="file" />
        </section>

        <section>
          <h2>Candidate Resumes</h2>
          <p>Upload one or more candidate resumes.</p>

          <input type="file" multiple />
        </section>

        <button>
          Rank Candidates
        </button>
      </main>
    </div>
  )
}

export default App