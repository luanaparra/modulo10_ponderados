import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;

class UploadImage extends StatefulWidget {
  @override
  _UploadImageState createState() => _UploadImageState();
}

class _UploadImageState extends State<UploadImage> {
  final ImagePicker _picker = ImagePicker();
  XFile? _image;

  Future<void> _pickImage() async {
    final pickedFile = await _picker.pickImage(source: ImageSource.gallery);
    setState(() {
      _image = pickedFile;
    });
  }

  Future<void> _uploadImage() async {
    if (_image == null) return;

    final request = http.MultipartRequest('POST', Uri.parse('http://localhost:8000/api/upload_image'));
    request.files.add(await http.MultipartFile.fromPath('file', _image!.path));

    final response = await request.send();

    if (response.statusCode == 200) {
      print('Imagem enviada com sucesso');
    } else {
      print('Falha ao enviar a imagem');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Upload de Imagem'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            _image == null ? Text('Nenhuma imagem selecionada') : Image.file(File(_image!.path)),
            SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: _pickImage,
              child: Text('Escolher Imagem'),
            ),
            SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: _uploadImage,
              child: Text('Enviar Imagem'),
            ),
          ],
        ),
      ),
    );
  }
}
