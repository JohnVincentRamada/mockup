<template>
    <div class="container mx-auto">
        <form v-on:submit.prevent="SubmitForm" enctype="multipart/form-data" class="update-profile p-4 shadow bg-body-tertiary rounded w-100">
            <h1>Update Profile</h1>
            <div class="password d-flex mb-3">
                <div class="col-md-6 p-1">
                    <label for="">First Name</label>
                    <input class="form-control" type="text" placeholder="John Vincent" v-model="form_account.first_name" required>
                </div>
                <div class="col-md-6 p-1">
                    <label for="">Last Name</label>
                    <input class="form-control" type="text" placeholder="Ramada" v-model="form_account.last_name" required>
                </div>
            </div>
            <div class="mb-3 row">
                <label class="col-sm-3" for="">Email</label>
                <div class="col-sm-9">
                    <input class="form-control" type="email" v-model="form_account.email" required>
                </div>
            </div>
            <div class="mb-3 row">
                <label class="col-sm-3" for="">Address</label>
                <div class="col-sm-9">
                    <input class="form-control" type="text" v-model="form_details.address" required>
                </div>
            </div>
            <div class="mb-3 row">
                <label class="col-sm-3" for="">Email</label>
                <div class="col-sm-9">
                    <input class="form-control" placeholder="ex. 9098763675" type="text" v-model="form_details.contact_number" required>
                </div>
            </div>
            <div class="mb-3 row">
                <label class="col-sm-4" for="">Profile Picture</label>
                <div class="col-sm-8">
                    <input type="file" id="avatar" name="avatar" v-on:change="onFileChange" accept="image/png, image/jpeg" />
                </div>
                
            </div>
            
                
            <button class="btn btn-outline-dark mt-2" type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default{
    data(){
        return{
            form_account: {
                first_name: '',
                last_name: '',
                email: '',
            },
            form_details: {
                address: '',
                contact_number: '',
                profile_picture: null,
            },
        }
    },
    mounted(){
        axios.get('/api/user/')
        .then(response => {
            this.form_account = response.data[0]
        })
        .catch(error => {
            console.log(error)
        })

        axios.get('/api/userdetail/')
        .then(response => {
            this.form_details = response.data[0]
        })
        .catch(error => {
            console.log(error)
        })
        
    },
    methods:{
        onFileChange(event) {
        const file = event.target.files[0];
        this.form_details.profile_picture = file;
        },
        
        async SubmitForm(){
            try {
            axios.put('/api/user/', this.form_account)
                
            const formData = new FormData();
            Object.entries(this.form_details).forEach(([key, value]) => {
            formData.append(key, value);
            });

            axios.put('/api/userdetail/', formData)
            .then(response => {
                console.log(response.data)
                this.$router.push({ name:'account' });
            })
            
            
            } catch (error) {
                console.log(error);
            }
        }
        
    }
}
</script>