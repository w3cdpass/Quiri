const express = require('express');
const cors = require('cors');

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.json({ status: 'online'})
})
// POST route
app.post('/message', (req, res) => {
    const { msg } = req.body;

    console.log('Received message:', msg);

    res.json({
        status: 'success',
        reply: `You sent: ${msg}`
    });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
