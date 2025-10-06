<template>
  <div class="app-container">
    <div class="card">
      <!-- Login -->
      <div v-if="showLogin">
        <h1 class="title">Iniciar Sesión</h1>
        <form @submit.prevent="loginUser" class="form">
          <input v-model="login.email" type="email" placeholder="Correo electrónico" required />
          <input v-model="login.password" type="password" placeholder="Contraseña" required />
          <button type="submit">Ingresar</button>
        </form>
        <p class="message">{{ loginMessage }}</p>
        <p class="toggle" @click="showLogin = false">
          ¿No tienes cuenta? <span>Regístrate aquí</span>
        </p>
      </div>

      <!-- Registro -->
      <div v-else>
        <h1 class="title">Registro</h1>
        <form @submit.prevent="registerUser" class="form">
          <input v-model="register.name" placeholder="Nombre" />
          <input v-model="register.email" type="email" placeholder="Correo electrónico" required />
          <input v-model="register.password" type="password" placeholder="Contraseña" required />
          <button type="submit">Registrar</button>
        </form>
        <p class="message">{{ registerMessage }}</p>
        <p class="toggle" @click="showLogin = true">
          ¿Ya tienes cuenta? <span>Inicia sesión</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backendUrl: "http://127.0.0.1:5000/api",
      showLogin: true,
      register: { email: "", password: "", name: "" },
      login: { email: "", password: "" },
      registerMessage: "",
      loginMessage: "",
    };
  },
  methods: {
    async registerUser() {
      const res = await fetch(`${this.backendUrl}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.register),
      });
      const data = await res.json();
      this.registerMessage = data.message || data.error;
    },
    async loginUser() {
      const res = await fetch(`${this.backendUrl}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.login),
      });
      const data = await res.json();
      this.loginMessage = data.message || data.error;
    },
  },
};
</script>

<style>
/* Importar tipografías */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display&family=Pinyon+Script&display=swap');

html, body, #app {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
}

.app-container {
  height: 100vh; /* ocupa toda la altura */
  width: 100vw;  /* ocupa todo el ancho */
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f5f0e6; /* Beige elegante */
  font-family: "Playfair Display", Georgia, serif;
}

/* Caja centrada */
.card {
  background: white;
  padding: 2.5rem 3rem;
  border-radius: 1rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  width: 380px;
  text-align: center;
}

/* Títulos con Pinyon Script */
.title {
  font-family: "Pinyon Script", cursive;
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #2c2c2c;
}

/* Formularios */
.form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

input {
  padding: 0.75rem;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  font-size: 1rem;
  font-family: inherit;
}

button {
  background: #3a3a3a;
  color: white;
  border: none;
  padding: 0.75rem;
  border-radius: 0.5rem;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

button:hover {
  background: #5a5a5a;
}

/* Mensajes */
.message {
  margin-top: 1rem;
  color: #555;
}

/* Texto de cambio login/registro */
.toggle {
  margin-top: 1.5rem;
  color: #666;
  cursor: pointer;
  font-size: 0.9rem;
}

.toggle span {
  color: #2c2c2c;
  font-weight: bold;
  text-decoration: underline;
}
</style>
