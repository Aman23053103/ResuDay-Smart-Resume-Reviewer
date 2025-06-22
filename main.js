// Dark Mode Toggle Handler
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.getElementById('darkModeToggle');

  toggle.addEventListener('change', () => {
    document.body.classList.toggle('dark');
  });

  // Form Submission Handler
  document.getElementById('reviewForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);

    try {
      const response = await fetch('/evaluate', {
        method: 'POST',
        body: formData
      });

      if (!response.ok) {
        throw new Error('Failed to evaluate. Server error.');
      }

      const data = await response.json();
      document.getElementById('result').innerHTML = data.result;
    } catch (error) {
      document.getElementById('result').innerHTML = `<p style="color:red;">${error.message}</p>`;
    }
  });
});
