PGDMP                          x            librarySystem    12.1    12.1                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16449    librarySystem    DATABASE     �   CREATE DATABASE "librarySystem" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_India.1252' LC_CTYPE = 'English_India.1252';
    DROP DATABASE "librarySystem";
                postgres    false            �            1259    16450    books1    TABLE     �   CREATE TABLE public.books1 (
    id text NOT NULL,
    title text,
    author text,
    stock integer,
    shelfnumber text,
    "Category" text
);
    DROP TABLE public.books1;
       public         heap    postgres    false            �            1259    16478    borrowed    TABLE     ~   CREATE TABLE public.borrowed (
    studentid text,
    bookid text,
    issuedate text,
    returndate text,
    fine real
);
    DROP TABLE public.borrowed;
       public         heap    postgres    false            �            1259    16490    reserved    TABLE     u   CREATE TABLE public.reserved (
    studentid text,
    bookid text,
    reservationdate text,
    expirydate text
);
    DROP TABLE public.reserved;
       public         heap    postgres    false            �            1259    24576    users    TABLE     x   CREATE TABLE public.users (
    studentid text NOT NULL,
    name1 text,
    branch text,
    currentallowed integer
);
    DROP TABLE public.users;
       public         heap    postgres    false                      0    16450    books1 
   TABLE DATA           S   COPY public.books1 (id, title, author, stock, shelfnumber, "Category") FROM stdin;
    public          postgres    false    202   �                 0    16478    borrowed 
   TABLE DATA           R   COPY public.borrowed (studentid, bookid, issuedate, returndate, fine) FROM stdin;
    public          postgres    false    203   �                 0    16490    reserved 
   TABLE DATA           R   COPY public.reserved (studentid, bookid, reservationdate, expirydate) FROM stdin;
    public          postgres    false    204   1                 0    24576    users 
   TABLE DATA           I   COPY public.users (studentid, name1, branch, currentallowed) FROM stdin;
    public          postgres    false    205   N       �
           2606    16457    books1 Books_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.books1
    ADD CONSTRAINT "Books_pkey" PRIMARY KEY (id);
 =   ALTER TABLE ONLY public.books1 DROP CONSTRAINT "Books_pkey";
       public            postgres    false    202            �
           2606    24583    users users_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (studentid);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    205               2  x�U��n� ��O���Y����h�&^�,�-��B�K�~P/�		'����?����.o��[�qA_"��N�^IH��4�&�nk/]K�+Y�[S�Jz4��\PKAx��\�^Y�"�+(�^�l�sP����3b���\x���(�]�ҡ��{D�hOg=��.�x:C}S�>W�\�����Z�*�ݗ�{uy�Q49� ��8��t2��Պn㦮0`wa3��3��"޺�&&�m�R'�:M��>�	1b	k�]a�{��>Ӆ�Zv�ɆY�)]XPK��O��&��}���J�,Q��         G   x�s�54�50�400�41�46�4�r�� ��9���)��T��Ҕ�Ԃ3�����q��AJc���� ��2            x������ � �         /   x�s�54�50����KLQ��H-J,�N,�trUp���4����� ��	�     